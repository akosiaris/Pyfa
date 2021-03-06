# Used by:
# Ships from group: Exhumer (4 of 4)
# Ships from group: Mining Barge (3 of 3)
type = "passive"
def handler(fit, container, context):
    level = fit.character.getSkill("Mining Barge").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting"),
                                  "duration", container.getModifiedItemAttr("shipBonusORE3") * level)