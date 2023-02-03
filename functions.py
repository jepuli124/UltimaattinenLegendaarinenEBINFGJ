def actionDoer(Actions):
    global PossibleActions
    for Action in Actions:
        if Action in PossibleActions:
            PossibleActions[Action]
    return