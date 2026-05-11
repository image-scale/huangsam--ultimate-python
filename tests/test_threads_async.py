"""Tests for thread and async modules."""

import asyncio

from pyguide.advanced.threads import (
    main as threads_main,
    Counter,
    SharedBuffer,
    delayed_multiply,
    run_with_threads,
    run_sequential,
    basic_thread_example,
)
from pyguide.advanced.async_patterns import (
    main as async_main,
    fetch_data,
    failing_task,
    basic_coroutine_patterns,
    concurrent_execution,
    task_cancellation,
    timeout_example,
    semaphore_example,
    exception_handling,
    task_group_example,
)


class TestThreadsModule:
    """Tests for the threads demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        threads_main()

    def test_counter_thread_safe(self):
        """Counter with lock should be thread-safe."""
        import threading

        counter = Counter()
        threads = []
        for _ in range(10):
            t = threading.Thread(target=counter.increment)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        assert counter.value == 10

    def test_counter_property(self):
        """Counter value property should work."""
        counter = Counter()
        assert counter.value == 0
        counter.increment()
        assert counter.value == 1

    def test_shared_buffer(self):
        """SharedBuffer should support put and get."""
        buffer = SharedBuffer(max_size=3)
        buffer.put(1)
        buffer.put(2)
        assert buffer.size() == 2
        assert buffer.get() == 1
        assert buffer.get() == 2
        assert buffer.size() == 0

    def test_delayed_multiply(self):
        """delayed_multiply should multiply by 2."""
        assert delayed_multiply(5, delay=0) == 10
        assert delayed_multiply(0, delay=0) == 0

    def test_thread_pool_results(self):
        """run_with_threads should produce correct results."""
        items = [1, 2, 3]
        results = run_with_threads(lambda x: x * 2, items)
        assert sorted(results) == [2, 4, 6]

    def test_sequential_results(self):
        """run_sequential should produce correct results."""
        items = [1, 2, 3]
        results = run_sequential(lambda x: x * 2, items)
        assert results == [2, 4, 6]

    def test_basic_thread_example(self):
        """basic_thread_example should run threads."""
        results = basic_thread_example()
        assert len(results) == 3


class TestAsyncModule:
    """Tests for the async patterns demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        async_main()

    def test_fetch_data(self):
        """fetch_data should return TaskResult."""
        result = asyncio.run(fetch_data("test", delay=0))
        assert result.task_id == "test"
        assert result.result == "data_test"

    def test_failing_task_fails(self):
        """failing_task should raise when should_fail=True."""
        try:
            asyncio.run(failing_task(should_fail=True))
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "failed" in str(e)

    def test_failing_task_succeeds(self):
        """failing_task should succeed when should_fail=False."""
        result = asyncio.run(failing_task(should_fail=False))
        assert result == "success"

    def test_basic_coroutine_patterns(self):
        """basic_coroutine_patterns should complete."""
        assert asyncio.run(basic_coroutine_patterns())

    def test_concurrent_execution_faster(self):
        """Concurrent execution should be faster than sequential."""
        seq_time, conc_time = asyncio.run(concurrent_execution())
        assert conc_time < seq_time

    def test_task_cancellation(self):
        """task_cancellation should cancel tasks."""
        assert asyncio.run(task_cancellation())

    def test_timeout_example(self):
        """timeout_example should handle timeouts."""
        assert asyncio.run(timeout_example())

    def test_semaphore_limits_concurrency(self):
        """semaphore_example should limit concurrency."""
        max_conc = asyncio.run(semaphore_example())
        assert max_conc <= 2

    def test_exception_handling(self):
        """exception_handling should handle exceptions."""
        assert asyncio.run(exception_handling())

    def test_task_group(self):
        """task_group_example should complete with results."""
        assert asyncio.run(task_group_example())

    def test_coroutine_detection(self):
        """iscoroutine should detect coroutines."""
        coro = fetch_data("test")
        assert asyncio.iscoroutine(coro)
        coro.close()

    def test_task_detection(self):
        """isfuture should detect tasks."""

        async def check_task():
            task = asyncio.create_task(fetch_data("test"))
            is_future = asyncio.isfuture(task)
            await task
            return is_future

        assert asyncio.run(check_task())
