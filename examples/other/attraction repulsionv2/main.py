from config import app, background_color
try:
    from .electron import Electron
    from .neutron import Neutron
    from .geohash import GeoHash
except:
    from electron import Electron
    from neutron import Neutron
    from geohash import GeoHash


neutrons = []
electrons = []
electrons_genhashs = {}
neutrons_genhashs = {}

def on_setup():
    app.no_stroke()
    app.smooth()
    global neutrons, electrons
    for _ in range(50):
        n = Neutron()
        neutrons.append(n)
        # if n.genhash_id not in neutrons_genhashs:
        #     neutrons_genhashs[n.genhash_id] = []
        # neutrons_genhashs[n.genhash_id].append(n)

    for _ in range(1500):
        e = Electron()
        electrons.append(e)
        if e.genhash_id not in electrons_genhashs:
            electrons_genhashs[e.genhash_id] = []
        electrons_genhashs[e.genhash_id].append(e)

def on_draw():
    app.background(*background_color)
    for i in neutrons:
        i.update(neutrons)
        i.display()
    for j in electrons:
        j.update(neutrons, electrons_genhashs)
        j.display()


app.regist_event('on_setup', on_setup)
app.regist_event('on_draw', on_draw)
app.loop()
