from fastapi import FastAPI, HTTPException

from hantek.driver import HantekDriver


app = FastAPI(
    title="Hantek API",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {
        "ok": True,
        "service": "Hantek API",
    }


@app.get("/capture")
def capture():
    driver = HantekDriver()

    try:
        driver.connect()

        driver.configure(
            sample_rate_index=0x04,
            voltage_range=0x01,
            channels=2,
        )

        ch1, ch2 = driver.capture(data_points=0x2000)

        return {
            "ok": True,
            "sampleRate": 1_000_000,
            "points": len(ch1),
            "ch1": list(ch1),
            "ch2": list(ch2),
        }

    except Exception as error:
        print(f"Capture error: {type(error).__name__}: {error}")

        raise HTTPException(
            status_code=500,
            detail=f"Ошибка получения данных: {type(error).__name__}: {error}",
        )

    finally:
        try:
            driver.close()
        except Exception as close_error:
            print(
                f"Close error: "
                f"{type(close_error).__name__}: {close_error}"
            )