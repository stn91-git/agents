export const APIRoutes = {
  GetPlaygroundAgents: (PlaygroundApiUrl: string) => {
    const url = `${PlaygroundApiUrl}/v1/playground/agents`;
    console.log('GetPlaygroundAgents URL:', url);
    return url;
  },
  AgentRun: (PlaygroundApiUrl: string) =>
    `${PlaygroundApiUrl}/v1/playground/agents/{agent_id}/runs`,
  PlaygroundStatus: (PlaygroundApiUrl: string) =>
    `${PlaygroundApiUrl}/v1/playground/status`,
  GetPlaygroundSessions: (PlaygroundApiUrl: string, agentId: string) =>
    `${PlaygroundApiUrl}/v1/playground/agents/${agentId}/sessions`,
  GetPlaygroundSession: (
    PlaygroundApiUrl: string,
    agentId: string,
    sessionId: string
  ) =>
    `${PlaygroundApiUrl}/v1/playground/agents/${agentId}/sessions/${sessionId}`,

  DeletePlaygroundSession: (
    PlaygroundApiUrl: string,
    agentId: string,
    sessionId: string
  ) =>
    `${PlaygroundApiUrl}/v1/playground/agents/${agentId}/sessions/${sessionId}`
}
