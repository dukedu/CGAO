# Architecture

```mermaid
flowchart TD

    Examples --> Services

    Services --> Crawler

    Crawler --> Pages

    Pages --> Parsers

    Parsers --> Models

    Models --> Exporters