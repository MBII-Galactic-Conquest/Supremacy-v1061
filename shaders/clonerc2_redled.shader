//REDLED

models/players/clonerc2/accessories_redled
{
    {
        map models/players/clonerc2/accessories_redled
        rgbGen lightingDiffuse
    }
    {
        map models/players/clonerc2/accessories-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
    {
        map models/players/clonerc2/accessories-glow-redled
        blendFunc GL_ONE GL_ONE
        glow
    }
}

models/players/clonerc2/backpack_redled
{
    {
        map models/players/clonerc2/backpack_redled
        rgbGen lightingDiffuse
    }
    {
        map models/players/clonerc2/backpack-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
    {
        map models/players/clonerc2/backpack-glow-redled
        blendFunc GL_ONE GL_ONE
        glow
    }
}

models/players/clonerc2/helmet_redled
{
	cull	twosided
    {
        map models/players/clonerc2/helmet_redled
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/clonerc2/helmet-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/clonerc2/visor_redled
{
    {
        map models/players/clonerc2/visor_redled
        blendFunc GL_DST_COLOR GL_ZERO
    }
    {
        map models/players/clonerc2/visor-spec-redled
        blendFunc GL_ONE GL_ONE
        glow
    }
}
