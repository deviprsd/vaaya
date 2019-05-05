from vaaya.utilities import asset_path


class Colors:
    primary = '#ABD3FB'
    secondary = '#CCE4F4'
    re_prim = '#abd5fe'
    text = '#EBEFF2'
    pm_dark = '#92B8D9'
    pm_light = '#9CC4E8'


class Shraavani:
    @classmethod
    def style_sheet(self):
        f = open(asset_path('qcss/shraavani.qcss'))
        try:
            qcss = f.read().format(
                primary=Colors.primary,
                secondary=Colors.secondary,
                text=Colors.text,
                re_prim=Colors.re_prim,
                pm_dark=Colors.pm_dark,
                pm_light=Colors.pm_light
            )
        except KeyError:
            qcss = ""
        f.close()
        return qcss
