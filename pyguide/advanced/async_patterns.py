"""
Asyncio provides an event loop for handling asynchronous operations,
making it ideal for I/O-bound tasks like network requests, file operations,
and database queries without the overhead of threads.

This module demonstrates:
1. Basic coroutines with async/await
2. Creating and managing tasks
3. Concurrent execution with gather
4. Task cancellation and timeouts
5. Semaphores for concurrency limits
6. Task groups for structured concurrency (Python 3.11+)
"""

import asyncio
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class TaskResult:
    """Result from an async task."""

    task_id: str
    started_at: datetime
    completed_at: datetime
    result: Any


async def fetch_data(task_id: str, delay: float = 0.01) -> TaskResult:
    """Simulate fetching data with a delay."""
    started = datetime.now()
    await asyncio.sleep(delay)
    completed = datetime.now()
    return TaskResult(
        task_id=task_id,
        started_at=started,
        completed_at=completed,
        result=f"data_{task_id}",
    )


async def failing_task(should_fail: bool = True) -> str:
    """Task that may fail."""
    await asyncio.sleep(0.001)
    if should_fail:
        raise ValueError("Task failed intentionally")
    return "success"


async def slow_task(duration: float = 1.0) -> str:
    """A slow task for timeout demonstration."""
    await asyncio.sleep(duration)
    return "slow_completed"


async def basic_coroutine_patterns():
    """Demonstrate basic coroutine patterns."""
    # A coroutine object is created but not executed until awaited
    coro = fetch_data("simple")
    assert asyncio.iscoroutine(coro)

    # Awaiting executes the coroutine
    result = await coro
    assert result.task_id == "simple"
    assert result.started_at < result.completed_at

    # Create a task for concurrent execution
    task = asyncio.create_task(fetch_data("task1"))
    assert asyncio.isfuture(task)

    # Await the task to get its result
    task_result = await task
    assert task_result.task_id == "task1"

    return True


async def concurrent_execution():
    """Demonstrate concurrent task execution with gather."""
    # Sequential execution (slow)
    sequential_start = datetime.now()
    results = []
    for i in range(5):
        results.append(await fetch_data(f"seq_{i}"))
    sequential_time = (datetime.now() - sequential_start).total_seconds()

    # Concurrent execution with gather (fast)
    concurrent_start = datetime.now()
    concurrent_results = await asyncio.gather(
        *[fetch_data(f"conc_{i}") for i in range(5)]
    )
    concurrent_time = (datetime.now() - concurrent_start).total_seconds()

    # Concurrent is faster
    assert concurrent_time < sequential_time
    assert len(concurrent_results) == 5

    return sequential_time, concurrent_time


async def task_cancellation():
    """Demonstrate task cancellation."""
    task = asyncio.create_task(slow_task(10.0))

    # Cancel the task
    await asyncio.sleep(0.01)
    task.cancel()

    cancelled = False
    try:
        await task
    except asyncio.CancelledError:
        cancelled = True

    assert cancelled
    assert task.cancelled()

    return True


async def timeout_example():
    """Demonstrate timeouts with wait_for."""
    # Task that completes within timeout
    fast_result = await asyncio.wait_for(fetch_data("fast"), timeout=1.0)
    assert fast_result is not None

    # Task that times out
    timed_out = False
    try:
        await asyncio.wait_for(slow_task(10.0), timeout=0.05)
    except asyncio.TimeoutError:
        timed_out = True

    assert timed_out

    return True


async def semaphore_example():
    """Demonstrate semaphores for concurrency limiting."""
    semaphore = asyncio.Semaphore(2)
    concurrent_count = 0
    max_concurrent = 0

    async def limited_task(task_id: str):
        nonlocal concurrent_count, max_concurrent
        async with semaphore:
            concurrent_count += 1
            max_concurrent = max(max_concurrent, concurrent_count)
            await asyncio.sleep(0.01)
            concurrent_count -= 1
            return task_id

    results = await asyncio.gather(*[limited_task(f"task_{i}") for i in range(10)])

    assert len(results) == 10
    assert max_concurrent <= 2

    return max_concurrent


async def exception_handling():
    """Demonstrate exception handling in concurrent tasks."""
    # gather with return_exceptions=True
    results = await asyncio.gather(
        failing_task(should_fail=True),
        failing_task(should_fail=False),
        failing_task(should_fail=True),
        return_exceptions=True,
    )

    assert len(results) == 3
    exceptions = [r for r in results if isinstance(r, Exception)]
    successes = [r for r in results if not isinstance(r, Exception)]
    assert len(exceptions) == 2
    assert len(successes) == 1

    return True


async def task_group_example():
    """Demonstrate TaskGroup for structured concurrency (Python 3.11+)."""
    results = []

    async with asyncio.TaskGroup() as tg:
        for i in range(3):

            async def capture_result(idx):
                result = await fetch_data(f"group_{idx}")
                results.append(result)

            tg.create_task(capture_result(i))

    assert len(results) == 3

    return True


async def event_loop_info():
    """Get information about the event loop."""
    loop = asyncio.get_running_loop()
    assert isinstance(loop, asyncio.AbstractEventLoop)
    assert loop.is_running()

    return True


def main():
    # Basic coroutine patterns
    assert asyncio.run(basic_coroutine_patterns())

    # Concurrent execution is faster
    seq_time, conc_time = asyncio.run(concurrent_execution())
    assert conc_time < seq_time

    # Task cancellation
    assert asyncio.run(task_cancellation())

    # Timeout handling
    assert asyncio.run(timeout_example())

    # Semaphore limits concurrency
    max_conc = asyncio.run(semaphore_example())
    assert max_conc <= 2

    # Exception handling
    assert asyncio.run(exception_handling())

    # TaskGroup structured concurrency
    assert asyncio.run(task_group_example())

    # Event loop information
    assert asyncio.run(event_loop_info())


if __name__ == "__main__":
    main()
