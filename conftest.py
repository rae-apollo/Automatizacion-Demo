import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Extraer Status Code o Código de Reserva desde user_properties
        status_code = "N/A"
        for prop in item.user_properties:
            if isinstance(prop, tuple) and len(prop) == 2:
                if prop[0] in ("status_code", "codigo_reserva"):
                    status_code = prop[1]
                    break
        report.status_code = status_code


def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Status Code</th>")
    cells.insert(2, "<th>Source</th>")


def pytest_html_results_table_row(report, cells):
    # 1. Muestra el código de estado (200, N/A, o el número de reserva "1796743")
    status = getattr(report, "status_code", "N/A")
    cells.insert(1, f"<td>{status}</td>")

    # 2. Evaluar Source
    node_id = getattr(report, "nodeid", "").lower().replace("\\", "/")
    file_path = str(getattr(report, "fspath", "")).lower().replace("\\", "/")

    if (
        "api" in node_id
        or "api" in file_path
        or file_path.startswith("test_")
    ):
        if "tests/" in node_id or "tests/" in file_path:
            source_val = "WEB CLIENTES"
        else:
            source_val = "API"
    else:
        source_val = "WEB CLIENTES"

    cells.insert(2, f"<td>{source_val}</td>")