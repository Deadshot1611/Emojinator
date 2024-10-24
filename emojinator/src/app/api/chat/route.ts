// app/api/chat/route.ts
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
    const { text } = await request.json();

    try {
        const response = await fetch("http://localhost:8000/generate_response", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text }),
        });

        const data = await response.json();
        return NextResponse.json(data);
    } catch (error) {
        return NextResponse.json({ error: "Failed to fetch response" }, { status: 500 });
    }
}
