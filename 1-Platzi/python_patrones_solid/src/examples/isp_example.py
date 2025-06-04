"""
Interface Segregation Principle (ISP) Examples

"Clients should not be forced to depend upon interfaces they do not use."

ISP suggests that it's better to have many small, specific interfaces
rather than one large, general-purpose interface.
"""

from abc import ABC, abstractmethod
from typing import List, Optional


# ========================================
# ❌ VIOLATES Interface Segregation Principle
# ========================================

class WorkerViolatesISP(ABC):
    """
    ❌ This interface violates ISP because it forces all workers
    to implement methods they might not need or use.
    """
    
    @abstractmethod
    def work(self) -> None:
        """All workers must work."""
        pass
    
    @abstractmethod
    def eat(self) -> None:
        """All workers must eat."""
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        """All workers must sleep."""
        pass
    
    @abstractmethod
    def code(self) -> None:
        """All workers must code."""
        pass
    
    @abstractmethod
    def attend_meetings(self) -> None:
        """All workers must attend meetings."""
        pass


class HumanWorkerViolatesISP(WorkerViolatesISP):
    """❌ Human worker - implements all methods appropriately."""
    
    def work(self) -> None:
        print("Human is working")
    
    def eat(self) -> None:
        print("Human is eating")
    
    def sleep(self) -> None:
        print("Human is sleeping")
    
    def code(self) -> None:
        print("Human is coding")
    
    def attend_meetings(self) -> None:
        print("Human is attending meetings")


class RobotWorkerViolatesISP(WorkerViolatesISP):
    """
    ❌ Robot worker - forced to implement methods it doesn't need.
    This violates ISP because robots don't eat or sleep.
    """
    
    def work(self) -> None:
        print("Robot is working")
    
    def eat(self) -> None:
        # ❌ Forced to implement even though robots don't eat
        raise NotImplementedError("Robots don't eat")
    
    def sleep(self) -> None:
        # ❌ Forced to implement even though robots don't sleep
        raise NotImplementedError("Robots don't sleep")
    
    def code(self) -> None:
        print("Robot is coding")
    
    def attend_meetings(self) -> None:
        # ❌ Robots might not need to attend meetings
        print("Robot is processing meeting data")


# ========================================
# ✅ FOLLOWS Interface Segregation Principle
# ========================================

# ✅ Small, focused interfaces
class Workable(ABC):
    """✅ Interface for entities that can work."""
    
    @abstractmethod
    def work(self) -> None:
        pass


class Eatable(ABC):
    """✅ Interface for entities that can eat."""
    
    @abstractmethod
    def eat(self) -> None:
        pass


class Sleepable(ABC):
    """✅ Interface for entities that can sleep."""
    
    @abstractmethod
    def sleep(self) -> None:
        pass


class Programmable(ABC):
    """✅ Interface for entities that can code."""
    
    @abstractmethod
    def code(self) -> None:
        pass


class MeetingAttendable(ABC):
    """✅ Interface for entities that can attend meetings."""
    
    @abstractmethod
    def attend_meetings(self) -> None:
        pass


# ✅ Classes implement only the interfaces they need
class HumanWorker(Workable, Eatable, Sleepable, Programmable, MeetingAttendable):
    """✅ Human implements all relevant interfaces."""
    
    def work(self) -> None:
        print("Human is working")
    
    def eat(self) -> None:
        print("Human is eating lunch")
    
    def sleep(self) -> None:
        print("Human is sleeping")
    
    def code(self) -> None:
        print("Human is writing Python code")
    
    def attend_meetings(self) -> None:
        print("Human is attending the daily standup")


class RobotWorker(Workable, Programmable):
    """✅ Robot only implements interfaces it actually uses."""
    
    def work(self) -> None:
        print("Robot is working 24/7")
    
    def code(self) -> None:
        print("Robot is generating optimized code")


class Manager(Workable, Eatable, Sleepable, MeetingAttendable):
    """✅ Manager implements interfaces relevant to management role."""
    
    def work(self) -> None:
        print("Manager is coordinating team activities")
    
    def eat(self) -> None:
        print("Manager is having a business lunch")
    
    def sleep(self) -> None:
        print("Manager is getting rest for tomorrow's decisions")
    
    def attend_meetings(self) -> None:
        print("Manager is leading the project review meeting")


# ========================================
# ADVANCED ISP EXAMPLE: Document Processor
# ========================================

# ❌ Fat interface that violates ISP
class DocumentProcessorViolatesISP(ABC):
    """❌ This interface forces all processors to implement everything."""
    
    @abstractmethod
    def read_document(self, path: str) -> str:
        pass
    
    @abstractmethod
    def write_document(self, path: str, content: str) -> bool:
        pass
    
    @abstractmethod
    def compress_document(self, path: str) -> bool:
        pass
    
    @abstractmethod
    def encrypt_document(self, path: str, key: str) -> bool:
        pass
    
    @abstractmethod
    def scan_for_viruses(self, path: str) -> bool:
        pass
    
    @abstractmethod
    def extract_metadata(self, path: str) -> dict:
        pass


# ✅ ISP-compliant interfaces
class DocumentReader(ABC):
    """✅ Interface for reading documents."""
    
    @abstractmethod
    def read_document(self, path: str) -> str:
        pass


class DocumentWriter(ABC):
    """✅ Interface for writing documents."""
    
    @abstractmethod
    def write_document(self, path: str, content: str) -> bool:
        pass


class DocumentCompressor(ABC):
    """✅ Interface for compressing documents."""
    
    @abstractmethod
    def compress_document(self, path: str) -> bool:
        pass


class DocumentEncryptor(ABC):
    """✅ Interface for encrypting documents."""
    
    @abstractmethod
    def encrypt_document(self, path: str, key: str) -> bool:
        pass


class VirusScanner(ABC):
    """✅ Interface for virus scanning."""
    
    @abstractmethod
    def scan_for_viruses(self, path: str) -> bool:
        pass


class MetadataExtractor(ABC):
    """✅ Interface for metadata extraction."""
    
    @abstractmethod
    def extract_metadata(self, path: str) -> dict:
        pass


# ✅ Specific implementations that only implement what they need
class PDFReader(DocumentReader):
    """✅ Simple PDF reader - only implements reading."""
    
    def read_document(self, path: str) -> str:
        print(f"Reading PDF document from {path}")
        return "PDF content extracted"


class TextDocumentProcessor(DocumentReader, DocumentWriter):
    """✅ Text processor - implements reading and writing."""
    
    def read_document(self, path: str) -> str:
        print(f"Reading text document from {path}")
        return "Text content"
    
    def write_document(self, path: str, content: str) -> bool:
        print(f"Writing text document to {path}")
        return True


class SecureDocumentProcessor(DocumentReader, DocumentWriter, DocumentEncryptor, VirusScanner):
    """✅ Secure processor - implements security-related features."""
    
    def read_document(self, path: str) -> str:
        print(f"Securely reading document from {path}")
        return "Secure content"
    
    def write_document(self, path: str, content: str) -> bool:
        print(f"Securely writing document to {path}")
        return True
    
    def encrypt_document(self, path: str, key: str) -> bool:
        print(f"Encrypting document {path} with key")
        return True
    
    def scan_for_viruses(self, path: str) -> bool:
        print(f"Scanning {path} for viruses")
        return True


class DocumentArchiver(DocumentReader, DocumentCompressor, MetadataExtractor):
    """✅ Archiver - implements compression and metadata extraction."""
    
    def read_document(self, path: str) -> str:
        print(f"Reading document for archiving: {path}")
        return "Document content for archiving"
    
    def compress_document(self, path: str) -> bool:
        print(f"Compressing document {path}")
        return True
    
    def extract_metadata(self, path: str) -> dict:
        print(f"Extracting metadata from {path}")
        return {"size": "10KB", "created": "2024-01-01", "author": "user"}


# ========================================
# REAL-WORLD EXAMPLE: Media Player
# ========================================

class MediaPlayable(ABC):
    """✅ Interface for basic media playback."""
    
    @abstractmethod
    def play(self) -> None:
        pass
    
    @abstractmethod
    def pause(self) -> None:
        pass
    
    @abstractmethod
    def stop(self) -> None:
        pass


class VolumeControllable(ABC):
    """✅ Interface for volume control."""
    
    @abstractmethod
    def set_volume(self, level: int) -> None:
        pass
    
    @abstractmethod
    def mute(self) -> None:
        pass


class PlaylistManageable(ABC):
    """✅ Interface for playlist management."""
    
    @abstractmethod
    def add_to_playlist(self, item: str) -> None:
        pass
    
    @abstractmethod
    def remove_from_playlist(self, item: str) -> None:
        pass


class EqualizerControllable(ABC):
    """✅ Interface for equalizer control."""
    
    @abstractmethod
    def set_equalizer(self, settings: dict) -> None:
        pass


class StreamingCapable(ABC):
    """✅ Interface for streaming capabilities."""
    
    @abstractmethod
    def stream_from_url(self, url: str) -> None:
        pass


# ✅ Different media players implement only needed interfaces
class BasicMediaPlayer(MediaPlayable, VolumeControllable):
    """✅ Basic player - only basic playback and volume."""
    
    def play(self) -> None:
        print("Playing media")
    
    def pause(self) -> None:
        print("Pausing media")
    
    def stop(self) -> None:
        print("Stopping media")
    
    def set_volume(self, level: int) -> None:
        print(f"Setting volume to {level}")
    
    def mute(self) -> None:
        print("Muting audio")


class AdvancedMediaPlayer(MediaPlayable, VolumeControllable, PlaylistManageable, EqualizerControllable):
    """✅ Advanced player with more features."""
    
    def play(self) -> None:
        print("Playing with advanced features")
    
    def pause(self) -> None:
        print("Pausing with fade effect")
    
    def stop(self) -> None:
        print("Stopping with cleanup")
    
    def set_volume(self, level: int) -> None:
        print(f"Setting volume to {level} with smooth transition")
    
    def mute(self) -> None:
        print("Muting with fade out")
    
    def add_to_playlist(self, item: str) -> None:
        print(f"Adding {item} to playlist")
    
    def remove_from_playlist(self, item: str) -> None:
        print(f"Removing {item} from playlist")
    
    def set_equalizer(self, settings: dict) -> None:
        print(f"Setting equalizer: {settings}")


class StreamingPlayer(MediaPlayable, VolumeControllable, StreamingCapable):
    """✅ Streaming player - focuses on streaming features."""
    
    def play(self) -> None:
        print("Playing streamed content")
    
    def pause(self) -> None:
        print("Pausing stream")
    
    def stop(self) -> None:
        print("Stopping stream")
    
    def set_volume(self, level: int) -> None:
        print(f"Setting stream volume to {level}")
    
    def mute(self) -> None:
        print("Muting stream")
    
    def stream_from_url(self, url: str) -> None:
        print(f"Streaming from {url}")


def demonstrate_isp():
    """Demonstrate the Interface Segregation Principle."""
    
    print("=== ISP Demonstration: Workers ===")
    
    # ✅ Each worker only implements what it needs
    workers = [
        HumanWorker(),
        RobotWorker(),
        Manager(),
    ]
    
    # All workers can work
    for worker in workers:
        if isinstance(worker, Workable):
            worker.work()
    
    print("\n=== ISP Demonstration: Document Processors ===")
    
    processors = [
        PDFReader(),
        TextDocumentProcessor(),
        SecureDocumentProcessor(),
        DocumentArchiver(),
    ]
    
    document_path = "example.pdf"
    
    for processor in processors:
        print(f"\nUsing {processor.__class__.__name__}:")
        
        # All processors can read
        if isinstance(processor, DocumentReader):
            content = processor.read_document(document_path)
        
        # Only some can write
        if isinstance(processor, DocumentWriter):
            processor.write_document("output.txt", "content")
        
        # Only some can compress
        if isinstance(processor, DocumentCompressor):
            processor.compress_document(document_path)
        
        # Only some can scan for viruses
        if isinstance(processor, VirusScanner):
            processor.scan_for_viruses(document_path)
    
    print("\n=== ISP Demonstration: Media Players ===")
    
    players = [
        BasicMediaPlayer(),
        AdvancedMediaPlayer(),
        StreamingPlayer(),
    ]
    
    for player in players:
        print(f"\nUsing {player.__class__.__name__}:")
        
        # All players have basic functionality
        player.play()
        player.set_volume(80)
        
        # Only advanced player has playlist management
        if isinstance(player, PlaylistManageable):
            player.add_to_playlist("Song 1")
        
        # Only streaming player can stream
        if isinstance(player, StreamingCapable):
            player.stream_from_url("https://stream.example.com/music")


if __name__ == "__main__":
    demonstrate_isp()


"""
🔍 ISP BENEFITS SUMMARY:

✅ BENEFITS OF FOLLOWING ISP:
1. REDUCED COUPLING: Classes depend only on interfaces they actually use
2. EASIER TESTING: Smaller interfaces are easier to mock and test
3. BETTER MODULARITY: Each interface has a single, focused responsibility
4. FLEXIBILITY: Easy to implement only needed functionality
5. MAINTAINABILITY: Changes to unused methods don't affect clients
6. CLEAR CONTRACTS: Interfaces express exactly what's needed

❌ PROBLEMS WITH VIOLATING ISP:
1. FORCED DEPENDENCIES: Classes must implement methods they don't need
2. UNNECESSARY COMPLEXITY: Implementing empty or exception-throwing methods
3. TIGHT COUPLING: Changes to any method affect all implementers
4. TESTING DIFFICULTIES: Must mock entire large interfaces
5. VIOLATION OF SINGLE RESPONSIBILITY: Large interfaces do too much

💡 ISP DESIGN GUIDELINES:
- Keep interfaces small and focused
- Group related methods together
- Use composition of multiple small interfaces
- Don't force clients to depend on unused methods
- Consider the client's perspective when designing interfaces
- Prefer role-based interfaces over feature-based ones
"""
