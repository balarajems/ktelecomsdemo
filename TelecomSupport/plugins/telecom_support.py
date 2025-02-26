# plugins/telecom_support.py

from typing import Annotated
from semantic_kernel.functions.kernel_function_decorator import kernel_function

class TelecomSupportPlugin:
    """Semantic Kernel Plugin for Telecom Support"""

    @kernel_function(name="network_summary", description="Summarizes network performance reports")
    async def network_summary(
        self,
        report_text: Annotated[str, "The network performance report text"]
    ) -> Annotated[str, "The summarized network report"]:
        """Summarizes network performance reports."""
        summary = report_text[:100] + "..." if len(report_text) > 100 else report_text
        return f"Summary of Network Report: {summary}"
