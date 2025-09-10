models/weapons2/laser_trap/body
{
	surfaceparm	nonopaque
	q3map_nolightmap
    {
        map models/weapons2/laser_trap_r/body
        rgbGen lightingDiffuse
    }
    {
        map models/weapons2/laser_trap_r/body_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
    {
        map models/weapons2/laser_trap_r/body_glow
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen identity
    }
}


models/weapons2/laser_trap/body_a
{
	surfaceparm	nonopaque
	q3map_nolightmap
    {
        map models/weapons2/laser_trap_r/body
        rgbGen lightingDiffuse
    }
    {
        map models/weapons2/laser_trap_r/body_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
    {
        map models/weapons2/laser_trap_r/body_glow
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen identity
    }
    {
        map models/weapons2/laser_trap_r/body_glow_a
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen wave sin 0 1 0.34 0.5
    }
    {
        map models/weapons2/laser_trap_r/body_glow_b
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen wave sin 0 1 0.66 0.5
    }
    {
        map models/weapons2/laser_trap_r/body_glow_c
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen wave sin 0 1 0.99 0.5
    }
}

models/weapons2/laser_trap/carrier
{
    surfaceparm nonopaque
    q3map_nolightmap
    {
        map models/weapons2/laser_trap_r/carrier
        rgbGen lightingDiffuse
    }
    {
        map models/weapons2/laser_trap_r/carrier_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}