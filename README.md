# Template Project: gRPC sending and saving JSONs files

Quick implementation of Google Remote Procedure Call (gRPC) Framework with string and JSON file handling.

---

## Initialization

1. Clone the repository:
    ```bash
    git clone https://github.com/Cybernetic-Ransomware/template_gRPC_JSON.git
    ```
2. Install Python >= 3.12.
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```
5. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply modifications to the `.proto` file.


7. Generate gRPC code:
    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hw.proto
    ```
8. Apply modifications to the `server.py` and `client.py` files.


9. Run the server and the client:
    ```bash
    python server.py
    python client.py
    ```

---

## Useful documentation

- gRPC: https://grpc.io/docs/languages/python/)
