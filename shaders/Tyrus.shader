models/players/tyrus/cape
{
	q3map_material	Fabric
	cull	disable
    {
        map models/players/tyrus/cape
        depthWrite
        rgbGen lightingDiffuse
    }
}

models/players/tyrus/backplate
{
	q3map_nolightmap
    {
        map models/players/tyrus/backplate
        rgbGen lightingDiffuse
    }
    {
        map models/players/tyrus/env
        blendFunc GL_SRC_ALPHA GL_ONE
        depthFunc equal
        detail
        tcGen environment
    }
}
models/players/tyrus/chest
{
	q3map_nolightmap
    {
        map models/players/tyrus/chest
        rgbGen lightingDiffuse
    }
    {
        map models/players/tyrus/env
        blendFunc GL_SRC_ALPHA GL_ONE
        depthFunc equal
        detail
        tcGen environment
    }
}
models/players/tyrus/torso_IK
{
	q3map_nolightmap
    {
        map models/players/tyrus/torso_IK
        rgbGen lightingDiffuse
    }
    {
        map models/players/tyrus/env
        blendFunc GL_SRC_ALPHA GL_ONE
        depthFunc equal
        detail
        tcGen environment
    }
}
models/players/tyrus/wrists
{
	q3map_nolightmap
    {
        map models/players/tyrus/wrists
        rgbGen lightingDiffuse
    }
    {
        map models/players/tyrus/env
        blendFunc GL_SRC_ALPHA GL_ONE
        depthFunc equal
        detail
        tcGen environment
    }
}
models/players/tyrus/winglet_r
{
	q3map_nolightmap
    {
        map models/players/tyrus/winglet_r
        rgbGen lightingDiffuse
    }
    {
        map models/players/tyrus/env
        blendFunc GL_SRC_ALPHA GL_ONE
        depthFunc equal
        detail
        tcGen environment
    }
}
models/players/tyrus/winglet_l
{
	q3map_nolightmap
    {
        map models/players/tyrus/winglet_l
        rgbGen lightingDiffuse
    }
    {
        map models/players/tyrus/env
        blendFunc GL_SRC_ALPHA GL_ONE
        depthFunc equal
        detail
        tcGen environment
    }
}


