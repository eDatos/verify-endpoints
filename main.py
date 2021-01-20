import verification
import notification


if __name__ == "__main__":
    failing_entrypoints = (
        verification.verify_entrypoints() + verification.verify_indicators()
    )
    if failing_entrypoints:
        notification.notify(failing_entrypoints)
