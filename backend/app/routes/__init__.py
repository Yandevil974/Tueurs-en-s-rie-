from . import (admin, auth, cases, counterfactuals, episodes, explore, media, memory, notifications, progress, reference, search)

ROUTERS = [
    auth.router,
    cases.router,
    episodes.router,
    counterfactuals.router,
    explore.router,
    memory.router,
    notifications.router,
    reference.router,
    search.router,
    progress.router,
    media.router,
    admin.router,
]

__all__ = ["ROUTERS"]
