FROM ubuntu:latest as compilesys

WORKDIR "/text_classification"

COPY text_classification /text_classification/text_classification
COPY main.py /text_classification
COPY spacy /text_classification/spacy
COPY BERT /text_classification/BERT
COPY train_BERT.py /text_classification
COPY poetry.lock /text_classification/poetry.lock
COPY pyproject.toml /text_classification/pyproject.toml
COPY docker-entrypoint.sh /text_classification/docker-entrypoint.sh

RUN mv /var/lib/apt/lists /var/lib/apt/oldlist
RUN mkdir -p /var/lib/apt/lists/partial
RUN apt-get clean
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    git


# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git .pyenv
ENV HOME  /text_classification
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.9.5
RUN pyenv global 3.9.5
RUN eval "$(/pyenv/bin/pyenv init -)"

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/text_classification/.local/bin:$PATH"
RUN poetry install

# Application environment variables
ENV WEB_SERVICE_PORT=10000

ENTRYPOINT ["sh", "docker-entrypoint.sh"]