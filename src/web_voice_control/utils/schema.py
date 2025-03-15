from pydantic import BaseModel, Field
from typing import Optional


class STTResponse(BaseModel):
    success: bool = Field(..., description="Whether the speech recognition was successful")
    error: Optional[str] = Field(None, description="Error message if an error occurred")
    transcription: Optional[str] = Field(None, description="Recognized text")
