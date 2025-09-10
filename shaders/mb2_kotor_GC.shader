
//// Old Republic Soldier ////
models/players/jpoldrepsold/helmet_copy
{
    cull twosided
    {
        map models/players/jpoldrepsold/helmet
        rgbGen lightingDiffuseEntity
    }
    {
        map models/players/jpoldrepsold/helmet_copy
        blendFunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
        rgbGen lightingDiffuse
    }
    {
        map models/players/jpoldrepsold/helmet_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/jpoldrepsold/torso_rgb
{
    cull twosided
    {
        map models/players/jpoldrepsold/torso_rgb
        rgbGen lightingDiffuseEntity
    }
    {
        map models/players/jpoldrepsold/torso_rgb
        blendFunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
        rgbGen lightingDiffuse
    }
    {
        map models/players/jpoldrepsold/torso_rgb
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/jpoldrepsold/legs_rgb
{
    cull twosided
    {
        map models/players/jpoldrepsold/legs_rgb
        rgbGen lightingDiffuseEntity
    }
    {
        map models/players/jpoldrepsold/legs_rgb
        blendFunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
        rgbGen lightingDiffuse
    }
    {
        map models/players/jpoldrepsold/legs_rgb
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/jpoldrepsold/boots_hips
{
    {
        map models/players/jpoldrepsold/boots_hips
        rgbGen lightingDiffuse
    }
    {
        map models/players/jpoldrepsold/boots_hips_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}
