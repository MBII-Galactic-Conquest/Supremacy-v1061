models/players/vong_shaper/hair
{
	q3map_nolightmap
	cull	disable
    {
        map models/players/vong_shaper/hair
        alphaFunc GE128
        blendFunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
        depthWrite
        rgbGen lightingDiffuse
    }
    {
        map models/players/vong_shaper/hair_spec
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
    }
}



models/players/vong_shaper/headkomari
{
    {
        map models/players/vong_shaper/headkomari
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/vong_shaper/headkomari
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/vong_shaper/bodyvosa
{
    {
        map models/players/vong_shaper/bodyvosa
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/vong_shaper/bodyvosa
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/vong_shaper/armmetal
{
        cull twosided
    {
        map models/players/vong_shaper/armmetal
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/vong_shaper/armmetal
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}

models/players/vong_shaper/arm
{
        cull twosided
    {
        map models/players/vong_shaper/arm
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/vong_shaper/arm
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}

models/players/vong_shaper/chest
{
        cull twosided
    {
        map models/players/vong_shaper/chest
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/vong_shaper/chest
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}

models/players/vong_shaper/wrist
{
        cull twosided
    {
        map models/players/vong_shaper/wrist
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/vong_shaper/wrist
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}

models/players/vong_shaper/metal
{
        cull twosided
    {
        map models/players/vong_shaper/metal
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/vong_shaper/metal
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}