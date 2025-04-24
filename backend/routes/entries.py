from fastapi import APIRouter, HTTPException
from typing import List
from models.entry import Entry
from database import entries_collection
from services.gemini import process_entry
from bson import ObjectId

router = APIRouter()

@router.post("/entries", response_model=Entry)
async def create_entry(entry: Entry):
    summary, mood_tag = await process_entry(entry.content)
    
    entry_dict = entry.dict()
    entry_dict["summary"] = summary
    entry_dict["mood_tag"] = mood_tag
    
    result = await entries_collection.insert_one(entry_dict)
    entry_dict["_id"] = str(result.inserted_id)
    
    return entry_dict

@router.get("/entries", response_model=List[Entry])
async def get_entries():
    entries = []
    async for entry in entries_collection.find().sort("created_at", -1):
        entry["_id"] = str(entry["_id"])
        entries.append(Entry(**entry))
    return entries 