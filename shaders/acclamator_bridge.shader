models/map_objects/imp_sd/console_8
{
    {
        map $lightmap
    }
    {
	 map models/map_objects/imp_sd/console_8
        blendFunc GL_DST_COLOR GL_ZERO
    }
	{
        map models/map_objects/imp_sd/console_8_glw
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen identity
    }
}

models/map_objects/imp_sd/console_7
{
    {
        map $lightmap
    }
    {
	 map models/map_objects/imp_sd/console_7
        blendFunc GL_DST_COLOR GL_ZERO
    }
	{
        map models/map_objects/imp_sd/console_7_glw
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen identity
    }
}

models/map_objects/imp_sd/console_3_low_res
{
    {
        map $lightmap
    }
    {
	 map models/map_objects/imp_sd/console_3_low_res
        blendFunc GL_DST_COLOR GL_ZERO
    }
	{
        map models/map_objects/imp_sd/console_3_low_res_glw
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen identity
    }
}

models/map_objects/imp_sd/console_1_low_res
{
    {
        map $lightmap
    }
    {
	 map models/map_objects/imp_sd/console_1_low_res
        blendFunc GL_DST_COLOR GL_ZERO
    }
	{
        map models/map_objects/imp_sd/console_1_low_res_glw
        blendFunc GL_ONE GL_ONE
        glow
        rgbGen identity
    }
}

models/map_objects/imp_sd/bridge_5
{
	q3map_material	SolidMetal
    {
        map $lightmap
    }
    {
        map models/map_objects/imp_sd/bridge_5
        blendFunc GL_DST_COLOR GL_ZERO
    }
    {
        map textures/imperial/env_shiny_floor
        blendFunc GL_SRC_ALPHA GL_ONE
        alphaGen const 0.25
        tcGen environment
    }
}

textures/doomgiver/DoorVSD
{
	qer_editorimage	textures/doomgiver/DoorVSD
    {
        map $lightmap
    }
    {
        map textures/doomgiver/DoorVSD
        blendFunc GL_DST_COLOR GL_ZERO
    }
    {
        map textures/doomgiver/DoorVSD_glow
        blendFunc GL_ONE GL_ONE
        glow
    }
}

textures/lw_skys/acclamator_sky
{
	qer_editorimage	textures/skies/sky.tga
	surfaceparm	sky
	surfaceparm	noimpact
	surfaceparm	nomarks
	notc
	q3map_nolightmap
	skyParms	textures/lw_skys/acclamator_sky 512 -
}
