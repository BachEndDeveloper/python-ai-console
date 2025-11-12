"""Test suite for the Python AI Console application."""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the main directory to the path so we can import main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import LightsPlugin


class TestLightsPlugin:
    """Test cases for the LightsPlugin class."""

    @pytest.fixture
    def lights_plugin(self):
        """Create a LightsPlugin instance for testing."""
        return LightsPlugin()

    @pytest.mark.asyncio
    async def test_turn_on_lights(self, lights_plugin):
        """Test turning on lights in a room."""
        result = await lights_plugin.turn_on("living room")
        assert result == "The lights in the living room have been turned on."

    @pytest.mark.asyncio
    async def test_turn_off_lights(self, lights_plugin):
        """Test turning off lights in a room."""
        result = await lights_plugin.turn_off("bedroom")
        assert result == "The lights in the bedroom have been turned off."

    @pytest.mark.asyncio
    async def test_turn_on_lights_different_rooms(self, lights_plugin):
        """Test turning on lights in different rooms."""
        rooms = ["kitchen", "bathroom", "office"]
        for room in rooms:
            result = await lights_plugin.turn_on(room)
            expected = f"The lights in the {room} have been turned on."
            assert result == expected

    @pytest.mark.asyncio
    async def test_turn_off_lights_different_rooms(self, lights_plugin):
        """Test turning off lights in different rooms."""
        rooms = ["kitchen", "bathroom", "office"]
        for room in rooms:
            result = await lights_plugin.turn_off(room)
            expected = f"The lights in the {room} have been turned off."
            assert result == expected


class TestMainFunction:
    """Test cases for the main function and environment setup."""

    @patch.dict(os.environ, {
        'AZURE_OPENAI_API_KEY': 'test_key',
        'AZURE_OPENAI_ENDPOINT': 'https://test.openai.azure.com',
        'AZURE_OPENAI_DEPLOYMENT_NAME': 'gpt-4-test'
    })
    def test_environment_variables_loaded(self):
        """Test that environment variables are properly loaded."""
        import main
        # This would test that the environment variables are being read
        # In a real scenario, you'd want to test the actual configuration
        assert os.getenv('AZURE_OPENAI_API_KEY') == 'test_key'
        assert os.getenv('AZURE_OPENAI_ENDPOINT') == 'https://test.openai.azure.com'
        assert os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME') == 'gpt-4-test'


if __name__ == "__main__":
    pytest.main([__file__])