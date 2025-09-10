models/players/T800/termhead
{
    {
        map models/players/T800/termhead
        rgbGen lightingDiffuse
    }
    {
        map models/players/T800/cm_baremetal
        blendFunc GL_DST_COLOR GL_SRC_COLOR
        tcGen environment
    }
    {
        map models/players/T800/termhead_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/T800/body
{
    {
        map models/players/T800/body
        rgbGen lightingDiffuse
    }
    {
        map models/players/T800/cm_baremetal
        blendFunc GL_DST_COLOR GL_SRC_COLOR
        tcGen environment
    }
    {
        map models/players/T800/body_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}