FROM python:3

WORKDIR /usr/src/app

# 使用するパッケージをインストール
RUN pip install click python-redmine

# ソースコードのインストール (作成コマンドを有効化)
COPY app /usr/src/app
RUN pip install --editable .

# 自動補完を有効化
RUN echo 'eval "$(_REDMINE_COMPLETE=source_bash redmine)"' >> ~/.bashrc

CMD [ "bash" ]