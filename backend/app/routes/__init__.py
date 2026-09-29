from . import cases, counterfactuals, episodes, explore, media, memory, reference, search

# Personal instance: account, subscription, notification and remote-progress routes
# are intentionally not mounted. Personal state stays in the browser on-device.
ROUTERS = [
    cases.router,
    episodes.router,
    counterfactuals.router,
    explore.router,
    memory.router,
    reference.router,
    search.router,
    media.router,
]

__all__ = ["ROUTERS"]
