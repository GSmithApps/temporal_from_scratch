- **What are the minimum four pieces of a temporal application?**
  - **My answer**: A workflow, a worker, a server/client, a workflow execution,
    a task queue, a workflow ID,
  - **Solution**: A Workflow Definition, an Activity Definition,
    A Worker to host the Activity and Workflow code, Some way to start the Workflow.
- **How does the Temporal server get information to the worker?**
  - **My answer**: the task queue and workflow ID
  - **Solution**: The Temporal Server adds Tasks to a Task Queue, and the Worker polls the Task Queue.
- **True or false, with the Temporal Python SDK, you define
  Workflow Definition by writing functions?**
  - **My answer**: False. Workflow Definitions are done by writing classes.
  - **Solution**: False. Workflow Definitions are classes.