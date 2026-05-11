"""
Weak references allow referencing objects without preventing garbage
collection. This is useful for caches, callbacks, and avoiding circular
references.

This module demonstrates:
1. Basic weak references with weakref.ref
2. WeakSet for collections of objects
3. WeakValueDictionary and WeakKeyDictionary
4. Weak references with callbacks
5. Proxy objects
"""

import gc
import weakref


class CacheableObject:
    """An object that can be cached."""

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"CacheableObject({self.name!r}, {self.value})"


class ObjectRegistry:
    """Registry that tracks objects using weak references."""

    def __init__(self):
        self._objects = weakref.WeakSet()
        self._removed_count = 0

    def register(self, obj):
        """Register an object in the registry."""
        self._objects.add(obj)

    def get_all(self):
        """Get all registered objects (that still exist)."""
        return set(self._objects)

    def count(self):
        """Get count of registered objects."""
        return len(self._objects)


class WeakCache:
    """Cache that uses weak references for values."""

    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def put(self, key: str, obj):
        """Add object to cache."""
        self._cache[key] = obj

    def get(self, key: str):
        """Get object from cache (may return None if collected)."""
        return self._cache.get(key)

    def keys(self):
        """Get all keys with live values."""
        return list(self._cache.keys())


class ObjectTracker:
    """Track objects with callbacks when they are collected."""

    def __init__(self):
        self.collected = []
        self._refs = {}

    def track(self, obj, name: str):
        """Track an object with a name."""

        def on_finalize(ref):
            self.collected.append(name)

        ref = weakref.ref(obj, on_finalize)
        self._refs[name] = ref

    def is_alive(self, name: str) -> bool:
        """Check if tracked object is still alive."""
        ref = self._refs.get(name)
        if ref is None:
            return False
        return ref() is not None


def basic_weak_reference():
    """Demonstrate basic weak reference behavior."""
    obj = CacheableObject("test", 42)
    ref = weakref.ref(obj)

    assert ref() is obj
    assert ref().value == 42

    del obj
    gc.collect()

    assert ref() is None
    return True


def weak_set_cleanup():
    """Demonstrate WeakSet automatic cleanup."""
    registry = ObjectRegistry()

    def create_objects():
        objects = [CacheableObject(f"obj_{i}", i) for i in range(5)]
        for obj in objects:
            registry.register(obj)
        return registry.count()

    count_inside = create_objects()
    assert count_inside == 5

    gc.collect()

    count_after = registry.count()
    assert count_after == 0

    return count_inside, count_after


def weak_value_dictionary():
    """Demonstrate WeakValueDictionary."""
    cache = WeakCache()

    obj1 = CacheableObject("first", 100)
    obj2 = CacheableObject("second", 200)

    cache.put("key1", obj1)
    cache.put("key2", obj2)

    assert cache.get("key1") is obj1
    assert cache.get("key2") is obj2
    assert len(cache.keys()) == 2

    del obj1
    gc.collect()

    assert cache.get("key1") is None
    assert cache.get("key2") is obj2
    assert len(cache.keys()) == 1

    return True


def weak_key_dictionary():
    """Demonstrate WeakKeyDictionary."""
    wkd = weakref.WeakKeyDictionary()

    key1 = CacheableObject("key1", 1)
    key2 = CacheableObject("key2", 2)

    wkd[key1] = "value1"
    wkd[key2] = "value2"

    assert wkd[key1] == "value1"
    assert len(wkd) == 2

    del key1
    gc.collect()

    assert len(wkd) == 1
    assert wkd[key2] == "value2"

    return True


def callback_on_collection():
    """Demonstrate callback when object is collected."""
    tracker = ObjectTracker()

    obj = CacheableObject("tracked", 99)
    tracker.track(obj, "my_object")

    assert tracker.is_alive("my_object")
    assert tracker.collected == []

    del obj
    gc.collect()

    assert not tracker.is_alive("my_object")
    assert "my_object" in tracker.collected

    return True


def proxy_object():
    """Demonstrate weak proxy objects."""
    obj = CacheableObject("proxied", 50)
    proxy = weakref.proxy(obj)

    assert proxy.name == "proxied"
    assert proxy.value == 50

    del obj
    gc.collect()

    try:
        _ = proxy.name
        return False
    except ReferenceError:
        return True


def main():
    # Basic weak reference
    assert basic_weak_reference()

    # WeakSet cleans up when objects are deleted
    inside, after = weak_set_cleanup()
    assert inside == 5
    assert after == 0

    # WeakValueDictionary drops entries when values are collected
    assert weak_value_dictionary()

    # WeakKeyDictionary drops entries when keys are collected
    assert weak_key_dictionary()

    # Callbacks fire when objects are collected
    assert callback_on_collection()

    # Proxy raises ReferenceError when object is gone
    assert proxy_object()

    # Strong reference prevents collection
    obj = CacheableObject("strong", 1)
    ref = weakref.ref(obj)
    gc.collect()
    assert ref() is obj

    # WeakSet drops objects when no strong references remain
    weak_set = weakref.WeakSet()

    temp_obj = CacheableObject("temp", 0)
    weak_set.add(temp_obj)
    assert len(weak_set) == 1

    del temp_obj
    gc.collect()

    assert len(weak_set) == 0


if __name__ == "__main__":
    main()
