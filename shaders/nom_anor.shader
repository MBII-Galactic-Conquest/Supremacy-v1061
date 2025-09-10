models/players/nom_anor/accessories
{
	cull	twosided
    {
        map models/players/nom_anor/accessories
        rgbGen lightingDiffuse
        //alphaFunc GE128
    }
    {
        map models/players/nom_anor/accessories
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen lightingSpecular
	detail
    }
}

models/players/nom_anor/basic_hand
{
	cull	twosided
    {
        map models/players/nom_anor/basic_hand
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/nom_anor/basic_hand
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/nom_anor/legs
{
	cull	twosided
    {
        map models/players/nom_anor/legs
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/nom_anor/legs
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/nom_anor/head
{
	cull	twosided
    {
        map models/players/nom_anor/head
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/nom_anor/head
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}

models/players/nom_anor/torso_arms
{
	cull	twosided
    {
        map models/players/nom_anor/torso_arms
        blendFunc GL_ONE GL_ZERO
        rgbGen lightingDiffuse
    }
    {
        map models/players/nom_anor/torso_arms
        blendFunc GL_SRC_ALPHA GL_ONE
        detail
        alphaGen lightingSpecular
    }
}