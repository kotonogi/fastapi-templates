# ベースとなるイメージの選択
FROM python:3.11

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY pyproject.toml .
COPY README.md .
RUN pip install --upgrade pip && \
    pip install  poetry && \
    python -m poetry config virtualenvs.create false && \
    poetry install
