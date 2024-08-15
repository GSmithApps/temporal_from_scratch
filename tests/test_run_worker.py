"""
Testing a worker.
"""


import uuid
from temporalio import activity
import pytest

from temporalio.worker import Worker
from temporalio.testing import WorkflowEnvironment

from activities import say_hello
from workflows import SayHello


@activity.defn(name="say_hello")
async def say_hello_mocked(name: str) -> str:
    return f"Hello, {name} from mocked activity!"

@pytest.mark.asyncio
async def test_mock_activity():
    task_queue_name = str(uuid.uuid4())
    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with Worker(
            env.client,
            task_queue=task_queue_name,
            workflows=[SayHello],
            activities=[say_hello_mocked]
        ):
            assert "Hello, World from mocked activity!" == await env.client.execute_workflow(
                SayHello.run,
                "World",
                id=str(uuid.uuid4()),
                task_queue=task_queue_name,
            )

