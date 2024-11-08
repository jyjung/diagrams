from . import _Security365

class _Cloud(_Security365):
    _type = "cloud"
    _icon_dir = "resources/security365/cloud"

# containerlinker.png  infolineage.png    security365.png   shieldgate.png  shieldinfo.png  shieldrive.png       shieldrm.png
# cypherdocsflow.png   remotebrowser.png  shieldexmail.png  shieldid.png    shieldmail.png  shieldriveworks.png  shieldshare.png

class ContainerLinker(_Cloud):
    _icon = "containerlinker.png"

class InfoLineage(_Cloud):
    _icon = "infolineage.png"

class Security365(_Cloud):
    _icon = "security365.png"

class ShieldGate(_Cloud):
    _icon = "shieldgate.png"

class ShieldInfo(_Cloud):
    _icon = "shieldinfo.png"

class Shieldrive(_Cloud):
    _icon = "shieldrive.png"

class Shieldrm(_Cloud):
    _icon = "shieldrm.png"

class CypherDocsFlow(_Cloud):
    _icon = "cypherdocsflow.png"

class RemoteBrowser(_Cloud):
    _icon = "remotebrowser.png"

class ShieldexMail(_Cloud):
    _icon = "shieldexmail.png"

class ShieldId(_Cloud):
    _icon = "shieldid.png"

class ShieldMail(_Cloud):
    _icon = "shieldmail.png"

class ShieldriveWorks(_Cloud):
    _icon = "shieldriveworks.png"

class ShieldShare(_Cloud):
    _icon = "shieldshare.png"






