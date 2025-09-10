models/players/rodian_stormtrooper/pauldron_rgb
{
    {
        map models/players/rodian_stormtrooper/pauldron_rgb
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuseEntity
    }
    {
        map models/players/rodian_stormtrooper/pauldron_rgb
        blendFunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
        rgbGen lightingDiffuse
    }
    {
        map models/players/rodian_stormtrooper/pauldron-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
        detail
    }
}
