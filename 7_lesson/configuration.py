import logging

# Configure logging for debugging and tracking operations
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Global configuration representing application settings
GLOBAL_CONFIG = {
    "feature_a": True,
    "feature_b": False,
    "max_retries": 3
}


class Configuration:
    def __init__(self, updates, validator=None):
        """Context manager for temporarily modifying the global configuration."""

        # Store the updates and the optional validator
        self.updates = updates
        self.validator = validator

        # To store the original state of the global configuration
        self.original_config = None

    def __enter__(self):
        """
        Enter the context: Apply the configuration updates.
        """

        # TODO: Save a copy of the current GLOBAL_CONFIG so it can be restored later.

        # TODO: Apply the updates to the GLOBAL_CONFIG.

        # TODO: Log the changes for debugging purposes.

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the context: Restore the original configuration and handle validation or exceptions.
        """

        # TODO: If a validator is provided, check the modified configuration.
        # If the validation fails, log the error and restore the original configuration.

        # TODO: If an exception occurs within the context block, ensure the original configuration is restored.

        # TODO: Log the restoration of the configuration for transparency.

# Example validator function (Optional)


def validate_config(config: dict) -> bool:
    """
    Example validator function to check the validity of the configuration.
    Returns True if the configuration is valid, False otherwise.
    """

    # TODO: Implement validation logic, e.g., ensure 'max_retries' is non-negative.


# Example usage (for students to test once implemented)
if __name__ == "__main__":
    logging.info("Initial GLOBAL_CONFIG: %s", GLOBAL_CONFIG)

    # Example 1: Successful configuration update
    try:
        # TODO: Use the Configuration context manager to update 'feature_a' and 'max_retries'
        with Configuration({"feature_a": False, "max_retries": 5}):
            logging.info("Inside context: %s", GLOBAL_CONFIG)
    except Exception as e:
        logging.error("Error: %s", e)

    logging.info("After context: %s", GLOBAL_CONFIG)

    # Example 2: Configuration update with validation failure
    try:
        # TODO: Use the Configuration context manager with invalid updates and a validator
        # to see how the context handles validation errors.
        with Configuration({"feature_a": "invalid_value", "max_retries": -1}, validator=validate_config):
            logging.info("This should not be printed if validation fails.")
    except Exception as e:
        logging.error("Caught exception: %s", e)

    logging.info("After failed context: %s", GLOBAL_CONFIG)
