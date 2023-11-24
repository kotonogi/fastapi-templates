import pytest


@pytest.mark.parametrize(
    "limit, offset, expect", [(5, 0, [1, 2, 3, 4, 5]), (5, 5, [6, 7, 8, 9, 10])]
)
def test_list_tasks(client, rollback, limit, offset, expect):
    from tests.factories import TasksFactory

    [TasksFactory(id=i, name=f"name-{i}") for i in range(1, 21)]

    response = client.get("/tasks/", params={"limit": limit, "offset": offset})
    data = response.json()

    assert response.status_code == 200

    assert len(data) == len(expect)
    for i, row in enumerate(data):
        assert row["id"] == expect[i]
        assert row["name"] == f"name-{expect[i]}"
