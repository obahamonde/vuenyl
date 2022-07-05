import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup,
} from 'unocss'

export default defineConfig({
  shortcuts: [
    ['btn', 'px-4 py-1 rounded inline-block cursor-pointer'],
    ['icon-btn', 'inline-block cursor-pointer select-none hover:scale-125 hover:ease-in-out hover:transition-all duration-200'],
    ['col', 'flex flex-col'],
    ['row', 'flex flex-row'],
    ['center', 'justify-center items-center'],
    ['tl', 'top-0 left-0 fixed'],
    ['tr', 'top-0 right-0 fixed'],
    ['bl', 'bottom-0 left-0 fixed'],
    ['br', 'bottom-0 right-0 fixed'],
    ['x1', 'h-1 w-1'],
    ['x2', 'h-2 w-2'],
    ['x4', 'h-4 w-4'],
    ['x6', 'h-6 w-6'],
    ['x8', 'h-8 w-8'],
    ['x10', 'h-10 w-10'],
    ['x12', 'h-16 w-16'],
    ['x16', 'h-16 w-16'],
    ['x24', 'h-24 w-24'],
    ['x32', 'h-32 w-32'],
    ['x48', 'h-48 w-48'],
    ['x64', 'h-64 w-64'],
    ['x96', 'h-96 w-96'],
    ['x128', 'h-128 w-128'],
    ['r','rounded'],
    ['r-f','rounded-full'],
    ['sh-lg','shadow-lg shadow-gray-500'],
    ['sh-md','shadow-md shadow-gray-500'],
    ['sh-sm','shadow-sm shadow-gray-500']
     ],
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons({
      scale: 1.2,
      warn: true,
    }),
    presetTypography(),
    presetWebFonts({
      fonts: {
        sans: 'DM Sans',
        serif: 'DM Serif Display',
        mono: 'DM Mono',
        script: 'Lobster'
      },
    }),
  ],
  transformers: [
    transformerDirectives(),
    transformerVariantGroup(),
  ],
  safelist: 'prose prose-sm m-auto text-left'.split(' '),
})
