"""Utility for sanitizing user input before passing to LLM prompts."""

import re

# Characters / patterns commonly used in prompt injection
_SUSPICIOUS_PATTERNS = re.compile(
    r"(?i)\b(ignore|forget|disregard|override|system\s*prompt|new\s*instructions"
    r"|you\s*are\s*now|act\s*as\s*if|pretend\s*that|do\s*not\s*follow)\b"
)


def sanitize_event(event: str) -> str:
    """Sanitize user-provided event text before injecting into prompts.

    Strips any prompt-injection attempts and limits length.
    """
    # Truncate at 500 chars
    sanitized = event.strip()[:500]

    # If suspicious patterns are detected, note it but still allow the content
    # (just flag it so the prompt can instruct the LLM appropriately)
    if _SUSPICIOUS_PATTERNS.search(sanitized):
        sanitized = _strip_injection_attempts(sanitized)

    return sanitized


def _strip_injection_attempts(text: str) -> str:
    """Remove lines that look like instruction overrides."""
    lines = text.splitlines()
    clean = [
        line
        for line in lines
        if not _SUSPICIOUS_PATTERNS.search(line)
    ]
    return "\n".join(clean).strip() or text[:100]
