models/players/imperialknight/cape
{
	q3map_material	Fabric
	cull	disable
    {
        map models/players/imperialknight/cape
        depthWrite
        rgbGen lightingDiffuse
    }
}

models/players/imperialknight/chest
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/chest
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/chest-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/imperialknight/bodysuit_up
{
	cull	disable
	q3map_material	Fabric
    {
        map models/players/imperialknight/bodysuit_up
        rgbGen lightingDiffuse
    }
}

models/players/imperialknight/torso_ik
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/torso_ik
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/torso_ik-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/imperialknight/winglet_l
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/winglet_l
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialknight/winglet-spec
        blendFunc GL_DST_COLOR GL_SRC_COLOR
        tcGen environment
    }
}
models/players/imperialknight/winglet_r
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/winglet_r
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialknight/winglet-spec
        blendFunc GL_DST_COLOR GL_SRC_COLOR
        tcGen environment
    }
}
models/players/imperialknight/arms
{
	cull	disable
    {
        map models/players/imperialknight/arms
        depthWrite
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/arms-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}
models/players/imperialknight/arms_insignia
{
	cull	disable
    {
        map models/players/imperialknight/arms_insignia
        depthWrite
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/arms-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }

}
models/players/imperialknight/backplate
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/backplate
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/backplate-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}
models/players/imperialknight/crotchplate
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/crotchplate
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/crotchplate-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}
models/players/imperialknight/handpad
{ 
	cull	disable
	q3map_nolightmap
    {
        map models/players/imperialknight/handpad
        rgbGen lightingDiffuse
    }
    {
        map models/players/imperialKnight/handpad-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/imperialknight/bodysuit_up
{ 
    {
        map models/players/imperialknight/bodysuit_up
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/imperialknight/bodysuit_up-spec
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}