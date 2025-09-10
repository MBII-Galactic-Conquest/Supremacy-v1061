models/players/skytrooper/sky
{
	cull	twosided
    {
        map models/players/skytrooper/sky
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/skytrooper/sky
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
    {
        map models/players/skytrooper/glow
        blendFunc GL_ONE GL_ONE
        detail
        rgbGen identity
    }
}