import os
import time
import asyncio
from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters
from support.file_size import get_size
from PDFNetPython3.PDFNetPython import *
from support.markups import close_button
from support.display_progress import progress_for_pyrogram


@Client.on_message(filters.private & filters.document)
async def compress_pdf(c, m: Message):
    msg = await m.reply_sticker("AnimatedSticker.tgs", reply_to_message_id=m.message_id)
    if not str(m.document.file_name).lower().endswith('.pdf'):
        await msg.edit(Presets.INVALID_FORMAT, reply_markup=close_button)
        return
    #
    dl_location = os.getcwd() + '/' + "downloads" + '/' + str(m.from_user.id) + '/'
    if not os.path.isdir(dl_location):
        os.makedirs(dl_location)
    else:
        for f in os.listdir(dl_location):
            try:
                os.remove(os.path.join(dl_location, f))
            except Exception:
                pass
    #
    await m.download(file_name=dl_location)
    
    # Let's find out the initial document size
    size_path = await get_size(dl_location)
    initial_size = size_path[0]
    #
    try:
        """
            I have used PDFNetPython3 package which found to be a better one to compress the pdf documents using python.
            Link: https://www.thepythoncode.com/article/compress-pdf-files-in-python
        """
        # Initialize the library
        PDFNet.Initialize()
        doc = PDFDoc(size_path[1])
        # Optimize PDF with the default settings
        doc.InitSecurityHandler()
        # Reduce PDF size by removing redundant information and compressing data streams
        Optimizer.Optimize(doc)
        doc.Save(size_path[1], SDFDoc.e_linearized)
        doc.Close()
    except Exception:
        await msg.delete()
        await m.reply_text(Presets.JOB_ERROR, reply_markup=close_button)
        return
    #
    await m.reply_document(
        document=size_path[1],
        reply_to_message_id=m.message_id,
        caption=m.caption if m.caption else ''
        )
    #
    try:
        os.remove(size_path[1])
    except Exception:
        pass
    #
    await msg.delete()
    await m.reply_text(Presets.FINISHED_JOB,
                   disable_web_page_preview=True,
                   reply_markup=close_button
                   )
