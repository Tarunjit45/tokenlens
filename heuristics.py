# Heuristics for detecting token waste.

# Rule: Redundant Instructions
# Wasted tokens are the sum of all instruction tokens after the first unique instruction.
def detect_redundant_instructions(all_calls):
    """
    Detects waste from repeated system prompts.
    
    Args:
        all_calls (list[LLMCallProfiler]): A list of profiler objects for all calls.

    Returns:
        int: Estimated number of wasted tokens from redundant instructions.
    """
    unique_prompts = set()
    wasted_tokens = 0
    for call in all_calls:
        prompt_content = call.system_prompt_content
        if prompt_content in unique_prompts:
            wasted_tokens += call.instruction_tokens
        else:
            unique_prompts.add(prompt_content)
    return wasted_tokens

# Rule: Bloated Context
# If context is > 60% of prompt tokens and completion is < 10% of context tokens,
# we estimate that 90% of the context was wasted.
def detect_bloated_context(call):
    """
    Detects waste from providing large context that is barely used.
    
    Args:
        call (LLMCallProfiler): The profiler object for a single call.

    Returns:
        int: Estimated number of wasted tokens from bloated context.
    """
    prompt_tokens = call.prompt_tokens
    context_tokens = call.context_tokens
    completion_tokens = call.completion_tokens

    if prompt_tokens == 0 or context_tokens == 0:
        return 0

    is_bloated = (context_tokens / prompt_tokens) > 0.6
    is_underused = (completion_tokens / context_tokens) < 0.1

    if is_bloated and is_underused:
        # Estimate that 90% of the context was waste.
        return int(context_tokens * 0.9)
    
    return 0

# Rule: Over-Verbose Output
# If completion is > 10x longer than the user query for non-creative tasks,
# we estimate that 80% of the completion tokens are waste.
def detect_over_verbosity(call):
    """
    Detects waste from outputs that are excessively long for the given task.
    
    Args:
        call (LLMCallProfiler): The profiler object for a single call.

    Returns:
        int: Estimated number of wasted tokens from over-verbose output.
    """
    task_type = call.call_data.get("task_type", "")
    query_tokens = call.user_query_tokens
    completion_tokens = call.completion_tokens

    if task_type == "creative" or query_tokens == 0:
        return 0

    is_oververbose = completion_tokens > (query_tokens * 10)

    if is_oververbose:
        # Estimate that 80% of the completion was waste.
        return int(completion_tokens * 0.8)
        
    return 0
