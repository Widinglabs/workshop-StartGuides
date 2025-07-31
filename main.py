from slide_agent.agent import SlideAgent


def main():
    """Simple agent application entry point."""
    print("🤖 Agent starting...")
    
    try:
        agent = SlideAgent()
        agent.run()
    except ValueError as e:
        print(f"❌ Error: {e}")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return
    
    print("✅ Agent ready")


if __name__ == "__main__":
    main()
