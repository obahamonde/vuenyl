import { type ViteSSGContext } from 'vite-ssg'

export type UserModule = (ctx: ViteSSGContext) => void

export type User = {
    uid?: string
    name?: string
    email: string
    avatar?: string
    token?: string
}

export type Message = {
    uid: string
    rid: string
    text: string
    timestamp: number
    read: boolean
}

export type Contact = {
    name: string
    email: string
    message: string
}

export type Product = {
    id: string
    title?: string
    subtitle?: string
    description?: string
    pictures?: string[]
    sample?: string
    price?: number
    currency?: string
    tags?: string[]
    category?: string
    stock?: number
    available?: boolean
}

export type Cart = {
    user: User
    items: {
        vuenyl: Vuenyl
        quantity: number
    }[]
    total: number
}

export type Vuenyl = {
    title: string
    genre: string
    price: number
    image: string
}

