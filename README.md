# Agent requests stasher.

## Запуск сервера.
Для первого запуска необходимо выполнить эту команду:

`docker compose up`

## Юнит тестирование сервера.

Для первого запуска тестов необходимо выполнить эту команду:

`docker-compose -f test.compose.yaml up --exit-code-from stash_holder__test --abort-on-container-exit`