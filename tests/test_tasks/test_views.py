class MockRepository:
    pass


def test_list_tasks(client, rollback, mocker):
    from tests.factories import TasksFactory

    class MockRepository:
        def list_tasks(self):
            return [TasksFactory(id=i, name=f"name-{i}") for i in range(1, 21)]

    mocker.patch(
        "fastapi_templates.services.tasks.api.get_tasks_repository",
        return_value=MockRepository(),
    )
    response = client.get("/tasks/", params={"limit": 0, "offset": 20})
    assert response.status_code == 200


def test_create_task(client, rollback, mocker):
    from tests.factories import TasksFactory

    class MockRepository:
        def create_task(self):
            return [TasksFactory(id=i, name=f"name-{i}") for i in range(1, 21)]

    mocker.patch(
        "fastapi_templates.services.tasks.api.get_tasks_repository",
        return_value=MockRepository(),
    )
    response = client.get("/tasks/", params={"limit": limit, "offset": offset})
    data = response.json()

    assert response.status_code == 200

    assert len(data) == len(expect)
    for i, row in enumerate(data):
        assert row["id"] == expect[i]
        assert row["name"] == f"name-{expect[i]}"
