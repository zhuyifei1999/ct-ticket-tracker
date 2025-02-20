# Emotes from https://discord.gg/kwcUuaK4rt
from bloonspy.model.btd6 import Relic, BossBloon


# Misc
X = "❌"
V = "✅"
ARROW_RIGHT = "▶️"
BLANK = "<:blank:1147902377748353075>"

# Leaderboard
TOP_1_GLOBAL = "<:t1global:1147903225702395964>"
TOP_2_GLOBAL = "<:t2global:1147903229103984721>"
TOP_3_GLOBAL = "<:t3global:1147903231821893824>"
TOP_25_GLOBAL = "<:t25global:1147903234648838154>"
TOP_1_PERCENT = "<a:t1percent:1148718396888858785>"
ECO = "🔺"
ECO_NEGATIVE = "🍃"
NEW_TEAM = "🆕"

# Planner
TILE_BANNER = "<:banner:1147904221497262173>"
TILE_RELIC = "<:relic:1147904264874758164>"
TILE_REGULAR = BLANK
RELICS = {  # If you're too lazy to replace all of these just delete all these keys except None
    Relic.ABILITIZED: "<:Abilitized:1147904304108290058>",
    Relic.AIR_AND_SEA: "<:AirAndSea:1147904326816251934>",
    Relic.ALCHEMIST_TOUCH: "<:AlchemistTouch:1147904436807663716>",
    Relic.BIGGER_BLOON_SABOTAGE: "<:BiggerBloonSabotage:1147904439429120120>",
    Relic.BOX_OF_CHOCOLATES: "<:BoxOfChocolates:1147904307644080259>",
    Relic.BOX_OF_MONKEY: "<:BoxOfMonkey:1147904329576095804>",
    Relic.BROKEN_HEART: "<:BrokenHeart:1147904332851847210>",
    Relic.CAMO_FLOGGED: "<:CamoFlogged:1147904335615885343>",
    Relic.CAMO_TRAP: "<:CamoTrap:1147904338166034542>",
    Relic.DEEP_HEAT: "<:DeepHeat:1147904341819269140>",
    Relic.DURABLE_SHOTS: "<:DurableShots:1147904310311649330>",
    Relic.EL_DORADO: "<:ElDorado:1147904345279569920>",
    Relic.EXTRA_EMPOWERED: "<:ExtraEmpowered:1147904442713251950>",
    Relic.FLINT_TIPS: "<:FlintTips:1147904347557089321>",
    Relic.FORTIFRIED: "<:Fortifried:1147904351591989248>",
    Relic.GLUE_TRAP: "<:GlueTrap:1147904354372825120>",
    Relic.GOING_THE_DISTANCE: "<:GoingTheDistance:1147904445879959644>",
    Relic.HARD_BAKED: "<:HardBaked:1147904448786616320>",
    Relic.HEARTLESS: "<:Heartless:1147904453144481902>",
    Relic.HERO_BOOST: "<:HeroBoost:1147904357845700669>",
    Relic.MAGIC_MONKEYS: "<:MagicMonkeys:1147904314006843502>",
    Relic.MANA_BULWARK: "<:ManaBulwark:1147904456583815340>",
    Relic.MARCHING_BOOTS: "<:MarchingBoots:1147904361326985397>",
    Relic.MILITARY_MONKEYS: "<:MoabMine:1147904459243012106>",
    Relic.MOAB_CLASH: "<:MoabClash:1147904317878177792>",
    Relic.MOAB_MINE: "<:MoabMine:1147904459243012106>",
    Relic.MONKEY_BOOST: "<:MonkeyBoost:1147904368092397668>",
    Relic.MONKEY_SHIELD: "<:MonkeyShield:1147904320407355412>",
    Relic.MONKEY_SHIELD_MARK2: "<:MonkeyShieldMark2:1147904371384922182>",
    Relic.MONKEY_SHIELD_MARK3: "<:MonkeyShieldMark3:1147904375419846748>",
    Relic.MONKEY_TYCOON: "<a:MonkeyTycoon:1148211283498385459>",
    Relic.OPEN_SEASON: "<:OpenSeason:1147904377764446218>",
    Relic.PRIMARY_PRIMATES: "<a:PrimaryPrimates:1148211292939751486>",
    Relic.PSI_VISION: "<:PsiVision:1147904383883952270>",
    Relic.REGENERATION: "<:Regeneration:1147904388413792286>",
    Relic.RESTORATION: "<:Restoration:1147904393111412837>",
    Relic.ROAD_SPIKES: "<:RoadSpikes:1147904397590937660>",
    Relic.ROUNDING_UP: "<:RoundingUp:1147904400749244427>",
    Relic.ROYAL_TREATMENT: "<a:RoyalTreatment:1148211295712194670>",
    Relic.SHARPSPLOSION: "<:Sharpsplosion:1147904405182623805>",
    Relic.STARTING_STASH: "<:StartingStash:1147904414942765187>",
    Relic.SMS: "<:Sms:1147904409754402947>",
    Relic.SUPPORT_SIMIANS: "<:SupportSimians:1147904323569848420>",
    Relic.TECHBOT: "<:Techbot:1147904425667592312>",
    Relic.THRIVE: "<:Thrive:1147904433519329401>",
    None: TILE_RELIC,
}
EXPIRE_STALE = "🔴"
EXPIRE_2HR = "🟠"
EXPIRE_3HR = "🟡"
EXPIRE_LATER = "🟢"
EXPIRE_AFTER_RESET = "⏩"
EXPIRE_DONT_RECAP = "⛔"

# Challenges
NO_KNOWLEDGE = "<a:no_knowledge:1148695588674732102>"
NO_SELLING = "<a:no_selling:1148694644239110237>"
MAX_TOWERS = "<a:max_towers:1148694639847673857>"
MOAB_HEALTH = "<a:moabhealth:1148694637255598170>"
CERAM_HEALTH = "<a:ceramhealth:1148694624945307648>"
BLOON_SPEED = "<a:bloonspeed:1148694620541288468>"
MOAB_SPEED = "<a:moabspeed:1148694638807498813>"
REGROW_RATE = "<a:regrowrate:1148694647691026433>"
VORTEX = "<a:vortex:1148694615952720044>"
BLOONARIUS = "<a:bloonarius:1148694617835970702>"
LYCH = "<a:lych:1148694634629959770>"
DREADBLOON = "<a:dreadbloon:1164867973807362068>"
PHAYZE = "<a:phayze:1164867969197817936>"
BOSSES = {
    BossBloon.VORTEX: "<a:vortex:1148694615952720044>",
    BossBloon.BLOONARIUS: "<a:bloonarius:1148694617835970702>",
    BossBloon.LYCH: "<a:lych:1148694634629959770>",
    BossBloon.DREADBLOON: "<a:dreadbloon:1164867973807362068>",
    BossBloon.PHAYZE: "<a:phayze:1164867969197817936>",
}
LEAST_CASH = "<a:leastcash:1148694630020435978>"
LEAST_TIERS = "<a:leasttier:1148694632969011332>"
TIME_ATTACK = "<a:Race:1148695164123095060>"
CASH = "<a:cash:1148694623192105010>"
