from fastapi import FastAPI
from hantek.driver import HantekDriver

app = FastAPI(
    title="Hantek API",
    version="1.0.0",
)

driver = HantekDriver()


@app.on_event("startup")
def startup():
    print("Connecting Hantek...")
    driver.connect()
    driver.configure(
        sample_rate_index=0x04,
        voltage_range=0x01,
        channels=2,
    )
    print("Hantek ready")


@app.on_event("shutdown")
def shutdown():
    driver.close()


@app.get("/capture")
def capture():

    ch1, ch2 = driver.capture(data_points=0x2000)

    return {
        "sampleRate": 1000000,
        "points": len(ch1),
        "ch1": list(ch1),
        "ch2": list(ch2),
    }