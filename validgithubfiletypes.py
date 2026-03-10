class GitHubFileTypes:
    image_media_types = ['.png', '.gif', '.jpg', '.jpeg', '.svg', '.mp4', '.mov', '.webm']

    # Documents
    document_types = [
        '.pdf',
        '.docx', '.pptx', '.xlsx', '.xls', '.xlsm',
        '.odt', '.fodt', '.ods', '.fods', '.odp', '.fodp', '.odg', '.fodg', '.odf',
        '.rtf', '.doc'
    ]

    # Text & data
    text_data_types = ['.txt', '.md', '.copilotmd', '.csv', '.tsv', '.log', '.json', '.jsonc']

    # Development & code
    development_code_types = [
        '.c', '.cs', '.cpp', '.css', '.drawio', '.dmp', '.html', '.htm', '.java',
        '.js', '.ipynb', '.patch', '.php', '.cpuprofile', '.pdb', '.py', '.sh',
        '.sql', '.ts', '.tsx', '.xml', '.yaml', '.yml'
    ]

    # Archive & compressed
    archive_compressed_types = ['.zip', '.gz', '.tgz']

    # Communication & logs
    communication_logs_types = ['.debug', '.msg', '.eml']

    # Bitmap & TIFF
    bitmap_tiff_types = ['.bmp', '.tif', '.tiff']

    # Audio
    audio_types = ['.mp3', '.wav']

    # Combined master list (preserves order, removes duplicates)
    def combine_preserve_order(*lists):
        seen = set()
        combined = []
        for lst in lists:
            for ext in lst:
                if ext not in seen:
                    seen.add(ext)
                    combined.append(ext)
        return combined

    valid_github_file_types = combine_preserve_order(
        # image_media_types,
        document_types,
        text_data_types,
        development_code_types,
        # archive_compressed_types,
        communication_logs_types,
        # bitmap_tiff_types,
        # audio_types
    )

    def exclude_types(self):
        
        exclude_from_context = ['.exe', '.dll', '.bin', '.iso', '.img', '.dmg', '.msi', '.apk', '.deb', '.rpm']

        for a in [self.bitmap_tiff_types,
            self.audio_types,
            self.image_media_types,
            self.archive_compressed_types
        ]:
            exclude_from_context.extend(a)  

        return exclude_from_context