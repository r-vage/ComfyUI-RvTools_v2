from ..core import CATEGORY

SAMPLERS_RESTART = ['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', \
                    'lms', 'dpmpp_2s_ancestral', 'dpmpp_2m', 'dpmpp_2m_alt', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'ddim']

class RvPasser_Sampler_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"sampler_name": (SAMPLERS_RESTART, {"forceInput": True}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value

    RETURN_TYPES = (SAMPLERS_RESTART,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "passthrough"

    def passthrough(self, sampler_name):
        return (sampler_name,)

NODE_NAME = 'Pass Sampler (Restart) [RvTools]'
NODE_DESC = 'Pass Sampler (Restart)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Sampler_Restart
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
