FROM mcr.microsoft.com/vscode/devcontainers/python

COPY . /workspaces/parcelona/
RUN pip3 --disable-pip-version-check --no-cache-dir install -e "/workspaces/parcelona/[dev]"