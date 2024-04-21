# fastapi_templates


## 構成

- サーバーフレームワーク: fastapi
- ORM: sqlmodel
- DB migration: alembic


## test

```
make test
```

## DBマイグレーション
```
# マイグレーションファイルの作成
make migration-file

# マイグレーションファイルのDBへの適用
make run_migration
```

## メモ

### alembic

### 初期化
`alembic init {ディレクトリ名}`で初期化とディレクトリ、ファイル作成
```
alembic init migrations
```

###  マイグレーションファイルの作成

マイグレーションファイルの作成は2種類の方法がある。

1. 空のマイグレーションファイルを作成 \
以下のコマンドで空のマイグレーションファイルを作成する.
```
alembic migration -m "{message}"
```


1. ORM用のdataクラスを参照する方法 \
sqlalchemyやsqlmodel用のdataクラスを参照する。\
env.py内のメタデータの参照先をそれぞれのクラスのメタデータに修正する \

sqlmodelを使用する際のenv.pyの記載例
``` python
import os
from logging.config import fileConfig

import pymysql
from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel
from toodo.models import Task

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata
```

また、sqlmodelのdataクラスを参照した際にマイグレーションファイルを作成すると、作成後のpythonファイルでsqlmodelがインポートされていない問題があるため`script.py.mako`に`import sqlmodel`を追加する

```
alembic migration --autogenerate -m "{message}"
```

###  マイグレーションファイルの実行
上記作業でマイグレーションファイルの作成を行った後
```
alembic upgrade head
```
でマイグレーションファイルの内容がDBに適用される。


