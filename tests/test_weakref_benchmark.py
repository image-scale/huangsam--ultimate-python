"""Tests for weak reference and benchmark modules."""

import gc
import weakref

from pyguide.advanced.weak_references import (
    main as weak_main,
    CacheableObject,
    ObjectRegistry,
    WeakCache,
    ObjectTracker,
    basic_weak_reference,
    weak_set_cleanup,
    weak_value_dictionary,
    weak_key_dictionary,
    callback_on_collection,
    proxy_object,
)
from pyguide.advanced.benchmarks import (
    main as bench_main,
    time_function,
    slow_fibonacci,
    cached_fibonacci,
    iterative_fibonacci,
    linear_search,
    binary_search,
    profile_function,
)


class TestWeakReferencesModule:
    """Tests for the weak references demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        weak_main()

    def test_cacheable_object(self):
        """CacheableObject should store name and value."""
        obj = CacheableObject("test", 42)
        assert obj.name == "test"
        assert obj.value == 42

    def test_object_registry_register(self):
        """ObjectRegistry should track objects."""
        registry = ObjectRegistry()
        obj = CacheableObject("obj", 1)
        registry.register(obj)
        assert registry.count() == 1
        assert obj in registry.get_all()

    def test_object_registry_cleanup(self):
        """ObjectRegistry should allow objects to be collected."""
        registry = ObjectRegistry()

        def add_temp():
            obj = CacheableObject("temp", 0)
            registry.register(obj)
            return registry.count()

        count_inside = add_temp()
        gc.collect()
        assert count_inside == 1
        assert registry.count() == 0

    def test_weak_cache(self):
        """WeakCache should store and retrieve objects."""
        cache = WeakCache()
        obj = CacheableObject("cached", 10)
        cache.put("key", obj)
        assert cache.get("key") is obj

    def test_weak_cache_cleanup(self):
        """WeakCache should drop entries when values are collected."""
        cache = WeakCache()
        obj = CacheableObject("temp", 5)
        cache.put("temp_key", obj)
        assert "temp_key" in cache.keys()
        del obj
        gc.collect()
        assert cache.get("temp_key") is None

    def test_object_tracker(self):
        """ObjectTracker should detect when objects are alive."""
        tracker = ObjectTracker()
        obj = CacheableObject("tracked", 1)
        tracker.track(obj, "my_obj")
        assert tracker.is_alive("my_obj")

    def test_object_tracker_callback(self):
        """ObjectTracker should record collections."""
        tracker = ObjectTracker()
        obj = CacheableObject("temp", 1)
        tracker.track(obj, "collected_obj")
        del obj
        gc.collect()
        assert "collected_obj" in tracker.collected

    def test_basic_weak_reference(self):
        """basic_weak_reference should demonstrate weak refs."""
        assert basic_weak_reference()

    def test_weak_set_cleanup(self):
        """weak_set_cleanup should show cleanup behavior."""
        inside, after = weak_set_cleanup()
        assert inside == 5
        assert after == 0

    def test_weak_value_dictionary(self):
        """weak_value_dictionary should work correctly."""
        assert weak_value_dictionary()

    def test_weak_key_dictionary(self):
        """weak_key_dictionary should work correctly."""
        assert weak_key_dictionary()

    def test_callback_on_collection(self):
        """callback_on_collection should fire callback."""
        assert callback_on_collection()

    def test_proxy_object(self):
        """proxy_object should raise ReferenceError."""
        assert proxy_object()


class TestBenchmarksModule:
    """Tests for the benchmarks demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        bench_main()

    def test_time_function(self):
        """time_function should return result and duration."""
        result, duration = time_function(lambda x: x * 2, 5)
        assert result == 10
        assert duration >= 0

    def test_slow_fibonacci(self):
        """slow_fibonacci should compute correct values."""
        assert slow_fibonacci(0) == 0
        assert slow_fibonacci(1) == 1
        assert slow_fibonacci(10) == 55

    def test_cached_fibonacci(self):
        """cached_fibonacci should compute correct values."""
        cached_fibonacci.cache_clear()
        assert cached_fibonacci(0) == 0
        assert cached_fibonacci(1) == 1
        assert cached_fibonacci(10) == 55

    def test_iterative_fibonacci(self):
        """iterative_fibonacci should compute correct values."""
        assert iterative_fibonacci(0) == 0
        assert iterative_fibonacci(1) == 1
        assert iterative_fibonacci(10) == 55

    def test_fibonacci_consistency(self):
        """All fibonacci implementations should agree."""
        cached_fibonacci.cache_clear()
        for n in range(15):
            slow = slow_fibonacci(n)
            cached = cached_fibonacci(n)
            iterative = iterative_fibonacci(n)
            assert slow == cached == iterative

    def test_linear_search(self):
        """linear_search should find elements."""
        items = [1, 3, 5, 7, 9]
        assert linear_search(items, 5) == 2
        assert linear_search(items, 1) == 0
        assert linear_search(items, 10) == -1

    def test_binary_search(self):
        """binary_search should find elements in sorted list."""
        items = [1, 3, 5, 7, 9]
        assert binary_search(items, 5) == 2
        assert binary_search(items, 1) == 0
        assert binary_search(items, 10) == -1

    def test_search_consistency(self):
        """Linear and binary search should find same indices."""
        items = list(range(100))
        for target in [0, 50, 99]:
            assert linear_search(items, target) == binary_search(items, target)

    def test_profile_function(self):
        """profile_function should return ProfileResult."""
        result = profile_function(slow_fibonacci, 10)
        assert result.call_count > 0
        assert result.total_time >= 0
        assert "slow_fibonacci" in result.stats_str

    def test_cached_faster_than_slow(self):
        """Cached fibonacci should be faster than slow."""
        cached_fibonacci.cache_clear()
        _, slow_time = time_function(slow_fibonacci, 20)
        _, cached_time = time_function(cached_fibonacci, 20)
        assert cached_time < slow_time

    def test_binary_faster_than_linear(self):
        """Binary search should be faster for large lists."""
        items = list(range(10000))
        _, linear_time = time_function(linear_search, items, 9999)
        _, binary_time = time_function(binary_search, items, 9999)
        assert binary_time < linear_time
