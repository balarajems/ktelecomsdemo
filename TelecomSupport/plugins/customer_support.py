# plugins/customer_support.py

from typing import Annotated
from semantic_kernel.functions.kernel_function_decorator import kernel_function

class CustomerSupportPlugin:
    """Semantic Kernel Plugin for Customer Support"""

    @kernel_function(name="sentiment_analysis", description="Analyzes customer sentiment")
    async def sentiment_analysis(
        self,
        message: Annotated[str, "The customer message text"]
    ) -> Annotated[str, "The sentiment of the message"]:
        """Analyzes the sentiment of the customer message."""
        text_lower = message.lower()
        if "happy" in text_lower or "satisfied" in text_lower:
            sentiment = "positive"
        elif "angry" in text_lower or "frustrated" in text_lower:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return f"Sentiment Analysis: {sentiment}"
